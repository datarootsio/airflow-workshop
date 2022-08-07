import * as trpc from "@trpc/server";
import { createRouter } from "./context";
import { z } from "zod";

import { OrderStatus, PizzaType } from "../../shared";

const BACKEND_SECRET = "DATAROOTS-PIZZERIA-123";

export const pizzaRouter = createRouter()
  .mutation("order", {
    meta: {
      openapi: {
        enabled: true,
        method: "POST",
        path: "/pizza/order",
        tag: "pizzeria-website",
        description: "Order a pizza.",
      },
    },
    input: z.object({
      pizzaType: PizzaType,
    }),
    output: z.object({
      orderId: z.number(),
    }),
    async resolve({ input, ctx }) {
      const pizza = await ctx.prisma.pizzaOrder.create({
        data: {
          pizzaType: input.pizzaType,
          orderStatus: OrderStatus.enum.Ordered,
        },
      });

      return {
        orderId: pizza.id,
      };
    },
  })
  .mutation("bake", {
    meta: {
      openapi: {
        enabled: true,
        method: "POST",
        path: "/pizza/bake",
        tag: "pizzeria-airflow",
        description: "Put 1 pizza in the oven.",
      },
    },
    input: z.object({}),
    output: z.object({
      orderId: z.number(),
    }),
    async resolve({ input, ctx }) {
      const pizzaOrder = await ctx.prisma.pizzaOrder.findFirst({
        where: { orderStatus: OrderStatus.enum.Ordered },
      });

      if (!pizzaOrder) {
        throw new trpc.TRPCError({
          code: "INTERNAL_SERVER_ERROR",
          message: "No pizza to bake :(",
        });
      }

      await ctx.prisma.pizzaOrder.update({
        where: { id: pizzaOrder.id },
        data: { orderStatus: OrderStatus.enum.Baking },
      });

      return {
        orderId: pizzaOrder.id,
      };
    },
  })
  .mutation("bake-batch", {
    meta: {
      openapi: {
        enabled: true,
        method: "POST",
        path: "/pizza/bake-batch",
        tag: "pizzeria-airflow",
        description: "Put 5 pizzas in the oven.",
      },
    },
    input: z.object({}),
    output: z.object({
      orderIds: z.array(z.number()),
    }),
    async resolve({ input, ctx }) {
      const batchSize = 5;

      const pizzaOrders = await ctx.prisma.pizzaOrder.findMany({
        take: batchSize,
        where: { orderStatus: OrderStatus.enum.Ordered },
      });

      if (pizzaOrders.length == 0) {
        throw new trpc.TRPCError({
          code: "INTERNAL_SERVER_ERROR",
          message: "No pizzas to bake :(",
        });
      }

      const pizzaOrdersIds = pizzaOrders.map((po) => po.id);

      await ctx.prisma.pizzaOrder.updateMany({
        where: { id: { in: pizzaOrdersIds } },
        data: { orderStatus: OrderStatus.enum.Baking },
      });

      return {
        orderIds: pizzaOrdersIds,
      };
    },
  })

  .mutation("send-for-delivery", {
    meta: {
      openapi: {
        enabled: true,
        method: "POST",
        path: "/pizza/send-for-delivery",
        tag: "pizzeria-airflow",
        description: "Send 1 pizza out for delivery.",
      },
    },
    input: z.object({
      orderId: z.number(),
    }),
    output: z.object({
      orderId: z.number(),
    }),
    async resolve({ input, ctx }) {
      const pizzaOrder = await ctx.prisma.pizzaOrder.findFirst({
        where: { id: input.orderId, orderStatus: OrderStatus.enum.Baked },
      });

      if (!pizzaOrder) {
        throw new trpc.TRPCError({
          code: "INTERNAL_SERVER_ERROR",
          message: "Pizza is not in correct order status or doesn't exist :(",
        });
      }

      await ctx.prisma.pizzaOrder.update({
        where: { id: pizzaOrder.id },
        data: { orderStatus: OrderStatus.enum.InDelivery },
      });

      return {
        orderId: pizzaOrder.id,
      };
    },
  })
  .mutation("oven", {
    meta: {
      openapi: {
        enabled: true,
        method: "POST",
        path: "/pizza/oven",
        tag: "pizzeria-authorized-personnel-only",
      },
    },
    input: z.object({ backend_secret: z.string() }),
    output: z.object({}),
    async resolve({ input, ctx }) {
      if (input.backend_secret != BACKEND_SECRET) {
        throw new trpc.TRPCError({
          code: "FORBIDDEN",
          message: "This is not for you!",
        });
      }

      const bakeChance = 0.1;

      const pizzaOrders = await ctx.prisma.pizzaOrder.findMany({
        where: { orderStatus: OrderStatus.enum.Baking },
      });

      for (const pizzaOrder of pizzaOrders) {
        if (Math.random() > bakeChance) {
          continue;
        }

        await ctx.prisma.pizzaOrder.update({
          where: { id: pizzaOrder.id },
          data: { orderStatus: OrderStatus.enum.Baked },
        });
      }

      return {};
    },
  })
  .mutation("deliver", {
    meta: {
      openapi: {
        enabled: true,
        method: "POST",
        path: "/pizza/deliver",
        tag: "pizzeria-authorized-personnel-only",
      },
    },
    input: z.object({ backend_secret: z.string() }),
    output: z.object({}),
    async resolve({ input, ctx }) {
      if (input.backend_secret != BACKEND_SECRET) {
        throw new trpc.TRPCError({
          code: "FORBIDDEN",
          message: "This is not for you!",
        });
      }

      const deliverChance = 0.1;

      const pizzaOrders = await ctx.prisma.pizzaOrder.findMany({
        where: { orderStatus: OrderStatus.enum.InDelivery },
      });

      for (const pizzaOrder of pizzaOrders) {
        if (Math.random() > deliverChance) {
          continue;
        }

        await ctx.prisma.pizzaOrder.update({
          where: { id: pizzaOrder.id },
          data: { orderStatus: OrderStatus.enum.Delivered },
        });
      }

      return {};
    },
  })
  .query("by-status", {
    meta: {
      openapi: {
        enabled: true,
        method: "GET",
        path: "/pizza/by-status",
        tag: "pizzeria-website",
        description: "Get all pizzas with a given status.",
      },
    },
    input: z.object({
      orderStatus: OrderStatus,
    }),
    output: z.array(
      z.object({
        id: z.number(),
        pizzaType: z.string(),
        orderStatus: z.string(),
      })
    ),
    async resolve({ input, ctx }) {
      const pizzaOrders = await ctx.prisma.pizzaOrder.findMany({
        where: {
          orderStatus: input.orderStatus,
        },
      });

      return pizzaOrders;
    },
  });
