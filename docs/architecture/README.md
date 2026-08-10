# Architecture

The repository is a monorepo with independent frontend and backend applications.

## MVP flow

1. Store staff manages categories, products, variants, prices and stock through Django Admin.
2. The React storefront reads the catalogue through versioned REST APIs.
3. Customers browse products, add SKU variants to cart and place orders.
4. Payments and shipping are integrated only after the catalogue and cart are stable.

## Principles

- Keep product variants and inventory at SKU level.
- Store money as fixed-precision decimal values, never floating point.
- Keep payment callbacks idempotent.
- Treat custom-curtain enquiries separately from standard product checkout.
- Keep the public brand name configurable until it is finalized.
