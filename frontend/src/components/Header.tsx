import { useState } from 'react'

type HeaderProps = {
  whatsapp: string
}

export default function Header({ whatsapp }: HeaderProps) {
  const [menuOpen, setMenuOpen] = useState(false)
  const closeMenu = () => setMenuOpen(false)

  return (
    <header className="header">
      <a className="brand" href="#top" onClick={closeMenu}>[BRAND NAME]</a>
      <button
        className="nav-toggle"
        aria-label={menuOpen ? 'Close menu' : 'Open menu'}
        aria-expanded={menuOpen}
        aria-controls="primary-nav"
        onClick={() => setMenuOpen((open) => !open)}
      >
        <span />
        <span />
        <span />
      </button>
      <nav id="primary-nav" aria-label="Primary navigation" className={menuOpen ? 'open' : ''}>
        <a href="#collections" onClick={closeMenu}>Collections</a>
        <a href="#custom" onClick={closeMenu}>Custom curtains</a>
        <a href="#gifting" onClick={closeMenu}>Gifting</a>
        <a href="#/products" onClick={closeMenu}>All Products</a>
      </nav>
      <a className="small-cta" href={`https://wa.me/${whatsapp}`}>WhatsApp us</a>
    </header>
  )
}
