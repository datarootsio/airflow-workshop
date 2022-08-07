import { createRouter } from "./context";
import { z } from "zod";

import { OrderStatus, PizzaType } from "../../shared";

export const pizzaRouter = createRouter().mutation("order", {
  meta: {
    openapi: { enabled: true, method: "POST", path: "/order", tag: "pizzeria" },
  },
  input: z.object({
    pizzaType: PizzaType,
  }),
  output: z.object({
    orderId: z.string(),
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
});
