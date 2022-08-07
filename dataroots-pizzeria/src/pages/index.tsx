import React, { useRef } from "react";

import type { NextPage } from "next";
import Head from "next/head";

import { PizzaOrder } from "@prisma/client";

import { trpc } from "../utils/trpc";
import { PizzaType, OrderStatus } from "../shared";

const OrderPizza: React.FC = () => {
  const pizzaTypeInput = useRef<HTMLSelectElement>(null);

  const client = trpc.useContext();
  const { mutate } = trpc.useMutation("pizza.order", {
    onSuccess: () => {
      client.invalidateQueries(["pizza.by-status"]);
    },
  });

  return (
    <div className="flex flex-row justify-between p-4 border-black border-2">
      <select
        className="w-3/5 border border-blue-500 rounded"
        ref={pizzaTypeInput}
        defaultValue=""
      >
        <option className="text-center" disabled value={""}>
          -- select a pizza --
        </option>
        {PizzaType.options.map((pizzaType) => (
          <option className="text-center" key={pizzaType} value={pizzaType}>
            {pizzaType}
          </option>
        ))}
      </select>
      <button
        className="ml-3 w-2/5 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
        onClick={() => {
          const selectedPizzaType = pizzaTypeInput.current?.value;
          if (!selectedPizzaType) {
            alert("Select a pizza");
            return;
          }

          const pizzaTypeOptions = PizzaType.options as string[];
          if (!pizzaTypeOptions.includes(selectedPizzaType)) {
            alert("Pizza type is wrong");
            return;
          }

          mutate({ pizzaType: selectedPizzaType as PizzaType });
          pizzaTypeInput.current!.value = "";
        }}
      >
        Order Pizza
      </button>
    </div>
  );
};

const PizzaOrdersByStatus: React.FC<{ orderStatus: OrderStatus }> = ({
  orderStatus,
}) => {
  const { data, isLoading } = trpc.useQuery(
    [
      "pizza.by-status",
      {
        orderStatus: orderStatus,
      },
    ],
    { refetchInterval: 1000 }
  );

  if (isLoading) return <div>Loading...</div>;

  return (
    <div className="w-full border-2 border-black">
      <div className="text-center underline font-bold">{orderStatus}</div>
      <hr />
      <div>
        {data?.length == 0 ? (
          <div className="text-center">No 🍕 here</div>
        ) : (
          data?.map((pizzaOrder) => (
            <PizzaOrderItem key={pizzaOrder.id} pizzaOrder={pizzaOrder} />
          ))
        )}
      </div>
    </div>
  );
};

const PizzaOrderItem: React.FC<{ pizzaOrder: PizzaOrder }> = ({
  pizzaOrder,
}) => {
  return (
    <div className="ml-5">
      {pizzaOrder.id} - {pizzaOrder.pizzaType}
    </div>
  );
};

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>Dataroots Pizzeria</title>
        <meta name="description" content="Dataroots Pizzeria" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="flex flex-col justify-center items-center p-10">
        <div className="w-1/2">
          <OrderPizza />
        </div>
        <div className="m-5 w-full flex flex-row justify-center">
          <PizzaOrdersByStatus orderStatus={OrderStatus.Values.Ordered} />
          <PizzaOrdersByStatus orderStatus={OrderStatus.Values.Baking} />
          <PizzaOrdersByStatus orderStatus={OrderStatus.Values.Baked} />
          <PizzaOrdersByStatus orderStatus={OrderStatus.Values.InDelivery} />
          <PizzaOrdersByStatus orderStatus={OrderStatus.Values.Delivered} />
        </div>
      </main>
    </>
  );
};

export default Home;
