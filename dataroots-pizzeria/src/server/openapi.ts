import { generateOpenApiDocument } from "trpc-openapi";

import { appRouter } from "./router/index";

export const openApiDocument = generateOpenApiDocument(appRouter, {
  title: "Dataroots Pizzeria CRUD API",
  description: "OpenAPI compliant REST API for the Dataroots Pizzeria",
  version: "1.0.0",
  baseUrl: "http://localhost:3000/api",
});
