import { createRouter } from "./context";
import { z } from "zod";

import { PizzaOrder } from "@prisma/client";

import { OrderStatus, PizzaType } from "../../shared";

export const pizzaRouter = createRouter()
  .mutation("order", {
    meta: {
      openapi: {
        enabled: true,
        method: "POST",
        path: "/pizza/order",
        tag: "pizzeria",
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
  .query("by-status", {
    meta: {
      openapi: {
        enabled: true,
        method: "GET",
        path: "/pizza/by-status",
        tag: "pizzeria",
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
