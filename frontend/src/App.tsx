import React, { useEffect, useState } from 'react'

type ProductVariant = {
  sku?: string
  size?: string
  colour?: string
  price?: string | number
  compare_at_price?: string | number
  stock_quantity?: number
}

type ProductImage = {
  id: number
  image?: string
  alt_text?: string
}

type Product = {
  id: number
  name: string
  short_name?: string
  slug: string
  sku?: string
  description?: string
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

type Category = {
  id: number
  name: string
  slug: string
  description?: string
}

const PRODUCT_API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'

export default function App() {
  const whatsapp = import.meta.env.VITE_WHATSAPP_NUMBER ?? '919999999999'
  const [view, setView] = useState<'home' | 'catalog' | 'detail'>('home')
  const [categories, setCategories] = useState<Category[]>([])
  const [products, setProducts] = useState<Product[]>([])
  const [selectedCategory, setSelectedCategory] = useState<string>('')
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  // Fetch categories on mount
  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await fetch(`${PRODUCT_API_URL}/categories/`)
        if (!response.ok) throw new Error('Unable to load categories')
        const data = await response.json()
        setCategories(data.results ?? data)
      } catch (err) {
        console.error('Category fetch error:', err)
      }
    }
    fetchCategories()
  }, [])

  // Fetch products when category changes
  useEffect(() => {
    const fetchProducts = async () => {
      if (view !== 'catalog') return
      setLoading(true)
      setError('')
      try {
        const url = selectedCategory
          ? `${PRODUCT_API_URL}/products/?category__slug=${selectedCategory}`
          : `${PRODUCT_API_URL}/products/`
        const response = await fetch(url)
        if (!response.ok) throw new Error('Unable to load products')
        const data = await response.json()
        setProducts(data.results ?? data)
      } catch (fetchError) {
        setError(fetchError instanceof Error ? fetchError.message : 'Failed to load products')
      } finally {
        setLoading(false)
      }
    }
    fetchProducts()
  }, [view, selectedCategory])

  const formatPrice = (price: string | number | undefined) => {
    if (!price) return 'Price on request'
    const numericPrice = Number(price)
    if (Number.isNaN(numericPrice)) return price
    return new Intl.NumberFormat('en-IN', {
      style: 'currency',
      currency: 'INR',
      maximumFractionDigits: 0,
    }).format(numericPrice)
  }

  const getProductPrice = (product: Product) => {
    return product.website_selling_price ?? product.variants?.[0]?.price ?? product.mrp ?? 0
  }

  const handleCategoryClick = (categorySlug: string) => {
    setSelectedCategory(categorySlug)
    setView('catalog')
    setSelectedProduct(null)
  }

  const handleProductClick = (product: Product) => {
    setSelectedProduct(product)
    setView('detail')
  }

  const handleBackToCatalog = () => {
    setView('catalog')
    setSelectedProduct(null)
  }

  return (
    <main>
      <header className="header">
        <a className="brand" href="#top" onClick={() => { setView('home'); setSelectedCategory(''); setSelectedProduct(null) }}>[BRAND NAME]</a>
        <nav aria-label="Primary navigation">
          <a href="#collections" onClick={() => setView('home')}>Collections</a>
          <a href="#custom" onClick={() => setView('home')}>Custom curtains</a>
          <a href="#gifting" onClick={() => setView('home')}>Gifting</a>
          <a href="#products" onClick={() => { setView('catalog'); setSelectedCategory('') }}>All Products</a>
        </nav>
        <a className="small-cta" href={`https://wa.me/${whatsapp}`}>WhatsApp us</a>
      </header>

      {view === 'home' && (
        <>
          <section className="hero" id="top">
            <div className="hero-copy">
              <p className="eyebrow">Home furnishings</p>
              <h1>Bring home colours that feel like you.</h1>
              <p className="lead">Curtains, fabrics, bedsheets, rugs and thoughtful gifts—chosen for Indian homes and everyday living.</p>
              <div className="actions">
                <button className="primary" onClick={() => { setView('catalog'); setSelectedCategory('') }}>Explore collections</button>
                <a className="secondary" href={`https://wa.me/${whatsapp}`}>Request assistance</a>
              </div>
            </div>
            <div className="hero-art" aria-label="Warm layered home textile composition">
              <div className="arch" />
              <div className="sun" />
              <div className="rug" />
              <div className="cushion one" />
              <div className="cushion two" />
            </div>
          </section>

          <section className="section" id="collections">
            <p className="eyebrow">Shop by category</p>
            <div className="section-heading">
              <h2>Everything that makes a house feel like home</h2>
              <p>Browse our collections by category or view all products.</p>
            </div>
            <div className="grid">
              {categories.map((category, index) => (
                <article
                  className={`card card-${(index % 6) + 1} clickable`}
                  key={category.slug}
                  onClick={() => handleCategoryClick(category.slug)}
                >
                  <span>{String((index % 6) + 1).padStart(2, '0')}</span>
                  <div><h3>{category.name}</h3><p>{category.description || 'Curated collection'}</p></div>
                </article>
              ))}
            </div>
          </section>

          <section className="feature" id="custom">
            <div><p className="eyebrow">Made for your space</p><h2>Custom curtains, without the guesswork.</h2></div>
            <p>Share your window measurements or arrange local assistance. We help select fabric, fall, lining and stitching.</p>
          </section>

          <section className="gift" id="gifting">
            <p className="eyebrow">The Sandook Collection</p>
            <h2>A home full of warmth, packed as a gift.</h2>
            <p>Premium bedsheet and pillow-cover sets in beautiful Sandook-style boxes for weddings, housewarmings and festivals.</p>
            <a className="primary" href={`https://wa.me/${whatsapp}`}>Enquire about gifting</a>
          </section>
        </>
      )}

      {view === 'catalog' && (
        <section className="catalog" id="products">
          <div className="catalog-header">
            <div>
              <p className="eyebrow">Live backend catalogue</p>
              <h2>{selectedCategory ? 'Category Products' : 'All Products'}</h2>
            </div>
            {selectedCategory && (
              <button className="filter-clear" onClick={() => setSelectedCategory('')}>Clear filter</button>
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
                <article
                  className="product-card clickable"
                  key={product.id}
                  onClick={() => handleProductClick(product)}
                >
                  <div className="product-image" aria-label={product.name}>
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
                      <button type="button" className="enquire-btn">View details</button>
                    </div>
                  </div>
                </article>
              ))}
            </div>
          )}
        </section>
      )}

      {view === 'detail' && selectedProduct && (
        <section className="product-detail">
          <button className="back-btn" onClick={handleBackToCatalog}>← Back to catalog</button>
          <div className="detail-container">
            <div className="detail-images">
              {selectedProduct.images && selectedProduct.images.length > 0 ? (
                <div className="image-gallery">
                  {selectedProduct.images.map((img, idx) => (
                    <div key={idx} className="gallery-item">
                      <img src={img.image} alt={img.alt_text || selectedProduct.name} />
                    </div>
                  ))}
                </div>
              ) : (
                <div className="image-placeholder">
                  <span>{selectedProduct.primary_colour || selectedProduct.primary_material || 'No image'}</span>
                </div>
              )}
            </div>
            <div className="detail-content">
              <span className="detail-tag">{selectedProduct.collection_name || selectedProduct.sub_category || 'Product'}</span>
              <h1>{selectedProduct.name}</h1>
              <p className="detail-sku">SKU: {selectedProduct.sku || 'N/A'}</p>
              
              <div className="detail-price">
                <span className="price-label">Price</span>
                <strong className="price-value">{formatPrice(getProductPrice(selectedProduct))}</strong>
                {selectedProduct.mrp && selectedProduct.website_selling_price && (
                  <span className="price-original">{formatPrice(selectedProduct.mrp)}</span>
                )}
              </div>

              <div className="detail-specs">
                <div className="spec-group">
                  <h3>Product Details</h3>
                  <ul>
                    <li><strong>Material:</strong> {selectedProduct.primary_material || selectedProduct.material || 'Not specified'}</li>
                    <li><strong>Print Pattern:</strong> {selectedProduct.print_pattern || 'Solid'}</li>
                    <li><strong>Print Technique:</strong> {selectedProduct.print_technique || 'Not specified'}</li>
                    <li><strong>Available Sizes:</strong> {selectedProduct.sizes_available || selectedProduct.length_drop || 'Custom available'}</li>
                    <li><strong>Colour:</strong> {selectedProduct.colour_family || selectedProduct.primary_colour || 'Not specified'}</li>
                    <li><strong>Current Stock:</strong> {selectedProduct.current_stock || 'Available'}</li>
                  </ul>
                </div>

                {selectedProduct.variants && selectedProduct.variants.length > 0 && (
                  <div className="spec-group">
                    <h3>Available Variants</h3>
                    <div className="variants-list">
                      {selectedProduct.variants.map((v, idx) => (
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

                {selectedProduct.description && (
                  <div className="spec-group">
                    <h3>Description</h3>
                    <p>{selectedProduct.description}</p>
                  </div>
                )}
              </div>

              <div className="detail-actions">
                <a href={`https://wa.me/${whatsapp}?text=Hi, I am interested in ${encodeURIComponent(selectedProduct.name)}`} className="primary">
                  Enquire via WhatsApp
                </a>
                <button className="secondary" onClick={handleBackToCatalog}>Continue shopping</button>
              </div>
            </div>
          </div>
        </section>
      )}

      <footer><strong>[BRAND NAME]</strong><span>Gujarat · India</span></footer>
    </main>
  )
}
