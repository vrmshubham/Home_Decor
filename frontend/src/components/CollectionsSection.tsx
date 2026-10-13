import type { Category } from '../types'

type CollectionsSectionProps = {
  categories: Category[]
  loading: boolean
  error: string
}

export default function CollectionsSection({ categories, loading, error }: CollectionsSectionProps) {
  return (
    <section className="section" id="collections">
      <p className="eyebrow">Shop by category</p>
      <div className="section-heading">
        <h2>Everything that makes a house feel like home</h2>
        <p>Browse our collections by category or view all products.</p>
      </div>
      {loading ? (
        <p className="status">Loading collections…</p>
      ) : error ? (
        <p className="status error">{error}</p>
      ) : (
        <div className="grid">
          {categories.map((category, index) => (
            <a
              className={`card card-${(index % 6) + 1} clickable`}
              key={category.slug}
              href={`#/products/category/${category.slug}`}
            >
              <span>{String((index % 6) + 1).padStart(2, '0')}</span>
              <div><h3>{category.name}</h3><p>{category.description || 'Curated collection'}</p></div>
            </a>
          ))}
        </div>
      )}
    </section>
  )
}
