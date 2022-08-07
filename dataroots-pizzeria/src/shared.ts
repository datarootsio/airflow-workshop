import { z } from "zod";

// export enum OrderStatus {
//   Ordered,
//   Baking,
//   Baked,
//   InDelivery,
//   Delivered,
// }

// export enum PizzaTypes {
//   Margherita = "Margherita",
//   V_Italy = "V-🇮🇹",
//   Hawai = "Hawaï",
// }

export const OrderStatus = z.enum([
  "Ordered",
  "Baking",
  "Baked",
  "InDelivery",
  "Delivered",
]);
export type OrderStatus = z.infer<typeof OrderStatus>;

export const PizzaType = z.enum(["Margherita", "V-🇮🇹", "Hawaï"]);
export type PizzaType = z.infer<typeof PizzaType>;
