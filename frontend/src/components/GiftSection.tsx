type GiftSectionProps = {
  whatsapp: string
}

export default function GiftSection({ whatsapp }: GiftSectionProps) {
  return (
    <section className="gift" id="gifting">
      <p className="eyebrow">The Sandook Collection</p>
      <h2>A home full of warmth, packed as a gift.</h2>
      <p>Premium bedsheet and pillow-cover sets in beautiful Sandook-style boxes for weddings, housewarmings and festivals.</p>
      <a className="primary" href={`https://wa.me/${whatsapp}`}>Enquire about gifting</a>
    </section>
  )
}
