# ADR 0001: Monorepo with catalogue-first MVP

## Decision

Use React and TypeScript for the storefront, Django REST Framework for APIs and administration, and PostgreSQL for production data.

The first milestone is catalogue management and product discovery. Cart, customer accounts, checkout, Razorpay and shipping integrations come after catalogue data is validated.

## Why

- Django Admin lets store staff begin entering products early.
- A catalogue-first launch can validate demand through WhatsApp enquiries.
- The architecture keeps frontend and backend independently deployable while sharing one repository.
