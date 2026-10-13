import type { Product } from './types'

export function formatPrice(price: string | number | undefined): string {
  if (!price) return 'Price on request'
  const numericPrice = Number(price)
  if (Number.isNaN(numericPrice)) return String(price)
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(numericPrice)
}

export function getProductPrice(product: Product): string | number {
  return product.website_selling_price ?? product.variants?.[0]?.price ?? product.mrp ?? 0
}
