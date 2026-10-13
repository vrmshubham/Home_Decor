type HeroProps = {
  whatsapp: string
}

export default function Hero({ whatsapp }: HeroProps) {
  return (
    <section className="hero" id="top">
      <div className="hero-copy">
        <p className="eyebrow">Home furnishings</p>
        <h1>Bring home colours that feel like you.</h1>
        <p className="lead">Curtains, fabrics, bedsheets, rugs and thoughtful gifts—chosen for Indian homes and everyday living.</p>
        <div className="actions">
          <a className="primary" href="#/products">Explore collections</a>
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
  )
}
