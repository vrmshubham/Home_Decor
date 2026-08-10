const categories = [
  { name: 'Curtains', note: 'Ready-made and custom stitched' },
  { name: 'Bedsheets', note: 'Everyday and premium collections' },
  { name: 'Rugs & Mats', note: 'For every room and entrance' },
  { name: 'Sofa Fabrics', note: 'Textures, prints and upholstery' },
  { name: 'Comforters', note: 'Soft layers for restful nights' },
  { name: 'Sandook Gifts', note: 'Festive sets, beautifully packed' },
]

export default function App() {
  const whatsapp = import.meta.env.VITE_WHATSAPP_NUMBER ?? '919999999999'

  return (
    <main>
      <header className="header">
        <a className="brand" href="#top">[BRAND NAME]</a>
        <nav aria-label="Primary navigation">
          <a href="#collections">Collections</a>
          <a href="#custom">Custom curtains</a>
          <a href="#gifting">Gifting</a>
        </nav>
        <a className="small-cta" href={`https://wa.me/${whatsapp}`}>WhatsApp us</a>
      </header>

      <section className="hero" id="top">
        <div className="hero-copy">
          <p className="eyebrow">Home furnishings · Bhavnagar</p>
          <h1>Bring home colours that feel like you.</h1>
          <p className="lead">Curtains, fabrics, bedsheets, rugs and thoughtful gifts—chosen for Indian homes and everyday living.</p>
          <div className="actions">
            <a className="primary" href="#collections">Explore collections</a>
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
          <p>Start with a curated catalogue. Online ordering and payments will follow after product data and stock are ready.</p>
        </div>
        <div className="grid">
          {categories.map((category, index) => (
            <article className={`card card-${index + 1}`} key={category.name}>
              <span>{String(index + 1).padStart(2, '0')}</span>
              <div><h3>{category.name}</h3><p>{category.note}</p></div>
            </article>
          ))}
        </div>
      </section>

      <section className="feature" id="custom">
        <div><p className="eyebrow">Made for your space</p><h2>Custom curtains, without the guesswork.</h2></div>
        <p>Share your window measurements or arrange local assistance in Bhavnagar. We help select fabric, fall, lining and stitching.</p>
      </section>

      <section className="gift" id="gifting">
        <p className="eyebrow">The Sandook Collection</p>
        <h2>A home full of warmth, packed as a gift.</h2>
        <p>Premium bedsheet and pillow-cover sets in beautiful Sandook-style boxes for weddings, housewarmings and festivals.</p>
        <a className="primary" href={`https://wa.me/${whatsapp}`}>Enquire about gifting</a>
      </section>

      <footer><strong>[BRAND NAME]</strong><span>Bhavnagar, Gujarat · India</span></footer>
    </main>
  )
}
