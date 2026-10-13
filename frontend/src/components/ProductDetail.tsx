import type { Product } from '../types'
import { formatPrice, getProductPrice } from '../format'

type ProductDetailProps = {
  product: Product | null
  loading: boolean
  error: string
  whatsapp: string
}

export default function ProductDetail({ product, loading, error, whatsapp }: ProductDetailProps) {
  const backHref = product?.category ? `#/products/category/${product.category}` : '#/products'

  if (loading) {
    return (
      <section className="product-detail">
        <a className="back-btn" href={backHref}>← Back to catalog</a>
        <p className="status">Loading product…</p>
      </section>
    )
  }

  if (error || !product) {
    return (
      <section className="product-detail">
        <a className="back-btn" href="#/products">← Back to catalog</a>
        <p className="status error">{error || 'Product not found.'}</p>
      </section>
    )
  }

  return (
    <section className="product-detail">
      <a className="back-btn" href={backHref}>← Back to catalog</a>
      <div className="detail-container">
        <div className="detail-images">
          {product.images && product.images.length > 0 ? (
            <div className="image-gallery">
              {product.images.map((img, idx) => (
                <div key={idx} className="gallery-item">
                  <img src={img.image} alt={img.alt_text || product.name} />
                </div>
              ))}
            </div>
          ) : (
            <div className="image-placeholder">
              <span>{product.primary_colour || product.primary_material || 'No image'}</span>
            </div>
          )}
        </div>
        <div className="detail-content">
          <span className="detail-tag">{product.collection_name || product.sub_category || 'Product'}</span>
          <h1>{product.name}</h1>
          <p className="detail-sku">SKU: {product.sku || 'N/A'}</p>

          <div className="detail-price">
            <span className="price-label">Price</span>
            <strong className="price-value">{formatPrice(getProductPrice(product))}</strong>
            {product.mrp && product.website_selling_price && (
              <span className="price-original">{formatPrice(product.mrp)}</span>
            )}
          </div>

          <div className="detail-specs">
            <div className="spec-group">
              <h3>Product Details</h3>
              <ul>
                <li><strong>Material:</strong> {product.primary_material || product.material || 'Not specified'}</li>
                <li><strong>Print Pattern:</strong> {product.print_pattern || 'Solid'}</li>
                <li><strong>Print Technique:</strong> {product.print_technique || 'Not specified'}</li>
                <li><strong>Available Sizes:</strong> {product.sizes_available || product.length_drop || 'Custom available'}</li>
                <li><strong>Colour:</strong> {product.colour_family || product.primary_colour || 'Not specified'}</li>
                <li><strong>Current Stock:</strong> {product.current_stock || 'Available'}</li>
              </ul>
            </div>

            {product.variants && product.variants.length > 0 && (
              <div className="spec-group">
                <h3>Available Variants</h3>
                <div className="variants-list">
                  {product.variants.map((v, idx) => (
                    <div key={idx} className="variant-item">
                      <span className="variant-size">{v.size || 'Standard'}</span>
                      <span className="variant-colour">{v.colour || 'Default'}</span>
                      <span className="variant-price">{formatPrice(v.price)}</span>
                      <span className="variant-stock">Stock: {v.stock_quantity || 'Available'}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {product.description && (
              <div className="spec-group">
                <h3>Description</h3>
                <p>{product.description}</p>
              </div>
            )}
          </div>

          <div className="detail-actions">
            <a href={`https://wa.me/${whatsapp}?text=Hi, I am interested in ${encodeURIComponent(product.name)}`} className="primary">
              Enquire via WhatsApp
            </a>
            <a className="secondary" href={backHref}>Continue shopping</a>
          </div>
        </div>
      </div>
    </section>
  )
}
