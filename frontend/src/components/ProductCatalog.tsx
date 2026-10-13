import type { Category, Product } from '../types'
import { formatPrice, getProductPrice } from '../format'

type ProductCatalogProps = {
  products: Product[]
  categories: Category[]
  categorySlug: string
  loading: boolean
  error: string
}

export default function ProductCatalog({ products, categories, categorySlug, loading, error }: ProductCatalogProps) {
  const categoryName = categorySlug
    ? categories.find((category) => category.slug === categorySlug)?.name ?? categorySlug
    : ''

  return (
    <section className="catalog" id="products">
      <div className="catalog-header">
        <div>
          <p className="eyebrow">Live backend catalogue</p>
          <h2>{categoryName || 'All Products'}</h2>
        </div>
        {categorySlug && (
          <a className="filter-clear" href="#/products">Clear filter</a>
        )}
      </div>

      {loading ? (
        <p className="status">Loading products…</p>
      ) : error ? (
        <p className="status error">{error}</p>
      ) : products.length === 0 ? (
        <p className="status">No products found in this category.</p>
      ) : (
        <div className="product-grid">
          {products.map((product) => (
            <a className="product-card clickable" key={product.id} href={`#/product/${product.slug}`}>
              <div className="product-image" aria-hidden="true">
                {product.images?.[0]?.image ? (
                  <img src={product.images[0].image} alt={product.images[0].alt_text || product.name} />
                ) : (
                  <span>{product.primary_colour || product.primary_material || 'Home'}</span>
                )}
              </div>
              <div className="product-body">
                <span className="product-tag">{product.collection_name || product.sub_category || 'Collection'}</span>
                <h3>{product.short_name || product.name}</h3>
                <p className="product-description">{product.print_pattern || product.primary_material || product.material || 'Curated home textile'}</p>
                <ul className="product-meta">
                  <li><strong>Material:</strong> {product.primary_material || product.material || 'Not specified'}</li>
                  <li><strong>Size:</strong> {product.sizes_available || product.length_drop || 'Custom size available'}</li>
                  <li><strong>Stock:</strong> {product.current_stock ?? product.variants?.[0]?.stock_quantity ?? 'Available'}</li>
                </ul>
                <div className="product-footer">
                  <strong>{formatPrice(getProductPrice(product))}</strong>
                  <span className="enquire-btn">View details</span>
                </div>
              </div>
            </a>
          ))}
        </div>
      )}
    </section>
  )
}
