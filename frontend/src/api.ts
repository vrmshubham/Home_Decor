import type { Category, Product } from './types'

export const PRODUCT_API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'

async function getJson<T>(url: string): Promise<T> {
  const response = await fetch(url)
  if (!response.ok) throw new Error(`Request to ${url} failed with status ${response.status}`)
  return response.json()
}

export async function fetchCategories(): Promise<Category[]> {
  const data = await getJson<{ results?: Category[] } | Category[]>(`${PRODUCT_API_URL}/categories/`)
  return Array.isArray(data) ? data : data.results ?? []
}

export async function fetchProducts(categorySlug?: string): Promise<Product[]> {
  const url = categorySlug
    ? `${PRODUCT_API_URL}/products/?category__slug=${encodeURIComponent(categorySlug)}`
    : `${PRODUCT_API_URL}/products/`
  const data = await getJson<{ results?: Product[] } | Product[]>(url)
  return Array.isArray(data) ? data : data.results ?? []
}

export async function fetchProductBySlug(slug: string): Promise<Product> {
  return getJson<Product>(`${PRODUCT_API_URL}/products/${encodeURIComponent(slug)}/`)
}
