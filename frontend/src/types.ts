export type ProductVariant = {
  sku?: string
  size?: string
  colour?: string
  price?: string | number
  compare_at_price?: string | number
  stock_quantity?: number
}

export type ProductImage = {
  id: number
  image?: string
  alt_text?: string
}

export type Product = {
  id: number
  name: string
  short_name?: string
  slug: string
  sku?: string
  description?: string
  category?: string
  sub_category?: string
  collection_name?: string
  primary_material?: string
  material?: string
  print_pattern?: string
  print_technique?: string
  primary_colour?: string
  colour_family?: string
  sizes_available?: string
  length_drop?: string
  website_selling_price?: string | number
  mrp?: string | number
  current_stock?: number
  variants?: ProductVariant[]
  images?: ProductImage[]
}

export type Category = {
  id: number
  name: string
  slug: string
  description?: string
}
