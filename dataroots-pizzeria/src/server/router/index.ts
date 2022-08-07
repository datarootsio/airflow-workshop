// src/server/router/index.ts
import { createRouter } from "./context";
import superjson from "superjson";

import { pizzaRouter } from "./pizza";

export const appRouter = createRouter()
  .transformer(superjson)
  .merge("pizza.", pizzaRouter);

// export type definition of API
export type AppRouter = typeof appRouter;
