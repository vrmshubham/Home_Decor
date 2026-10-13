import { useEffect, useState } from 'react'
import Header from './components/Header'
import Hero from './components/Hero'
import CollectionsSection from './components/CollectionsSection'
import FeatureSection from './components/FeatureSection'
import GiftSection from './components/GiftSection'
import ProductCatalog from './components/ProductCatalog'
import ProductDetail from './components/ProductDetail'
import Footer from './components/Footer'
import { useHashRoute } from './useHashRoute'
import { fetchCategories, fetchProductBySlug, fetchProducts } from './api'
import type { Category, Product } from './types'

export default function App() {
  const whatsapp = import.meta.env.VITE_WHATSAPP_NUMBER ?? '919999999999'
  const route = useHashRoute()

  const [categories, setCategories] = useState<Category[]>([])
  const [categoriesLoading, setCategoriesLoading] = useState(true)
  const [categoriesError, setCategoriesError] = useState('')

  const [products, setProducts] = useState<Product[]>([])
  const [productsLoading, setProductsLoading] = useState(false)
  const [productsError, setProductsError] = useState('')

  const [product, setProduct] = useState<Product | null>(null)
  const [productLoading, setProductLoading] = useState(false)
  const [productError, setProductError] = useState('')

  // Categories are needed on the homepage and to label the catalog, so load them once.
  useEffect(() => {
    let cancelled = false
    setCategoriesLoading(true)
    fetchCategories()
      .then((data) => { if (!cancelled) setCategories(data) })
      .catch((err) => { if (!cancelled) setCategoriesError(err instanceof Error ? err.message : 'Unable to load categories') })
      .finally(() => { if (!cancelled) setCategoriesLoading(false) })
    return () => { cancelled = true }
  }, [])

  useEffect(() => {
    if (route.view !== 'catalog') return
    let cancelled = false
    setProductsLoading(true)
    setProductsError('')
    fetchProducts(route.category)
      .then((data) => { if (!cancelled) setProducts(data) })
      .catch((err) => { if (!cancelled) setProductsError(err instanceof Error ? err.message : 'Failed to load products') })
      .finally(() => { if (!cancelled) setProductsLoading(false) })
    return () => { cancelled = true }
  }, [route.view, route.view === 'catalog' ? route.category : undefined])

  useEffect(() => {
    if (route.view !== 'detail') return
    let cancelled = false
    setProductLoading(true)
    setProductError('')
    setProduct(null)
    fetchProductBySlug(route.slug)
      .then((data) => { if (!cancelled) setProduct(data) })
      .catch((err) => { if (!cancelled) setProductError(err instanceof Error ? err.message : 'Failed to load product') })
      .finally(() => { if (!cancelled) setProductLoading(false) })
    return () => { cancelled = true }
  }, [route.view, route.view === 'detail' ? route.slug : undefined])

  // Same-page nav links (Collections, Custom curtains, Gifting) rely on the hash matching a
  // section id — restore that scroll once the homepage sections are back in the DOM.
  useEffect(() => {
    if (route.view !== 'home') return
    const hash = window.location.hash.replace(/^#/, '')
    if (!hash || hash === 'top') {
      window.scrollTo({ top: 0 })
      return
    }
    document.getElementById(hash)?.scrollIntoView({ block: 'start' })
  }, [route])

  return (
    <main>
      <Header whatsapp={whatsapp} />

      {route.view === 'home' && (
        <>
          <Hero whatsapp={whatsapp} />
          <CollectionsSection categories={categories} loading={categoriesLoading} error={categoriesError} />
          <FeatureSection />
          <GiftSection whatsapp={whatsapp} />
        </>
      )}

      {route.view === 'catalog' && (
        <ProductCatalog
          products={products}
          categories={categories}
          categorySlug={route.category}
          loading={productsLoading}
          error={productsError}
        />
      )}

      {route.view === 'detail' && (
        <ProductDetail product={product} loading={productLoading} error={productError} whatsapp={whatsapp} />
      )}

      <Footer />
    </main>
  )
}
