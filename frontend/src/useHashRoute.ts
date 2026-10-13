import { useEffect, useState } from 'react'

export type Route =
  | { view: 'home' }
  | { view: 'catalog'; category: string }
  | { view: 'detail'; slug: string }

function parseHash(hash: string): Route {
  const segments = hash.replace(/^#\/?/, '').split('/').filter(Boolean)

  if (segments[0] === 'products') {
    if (segments[1] === 'category' && segments[2]) {
      return { view: 'catalog', category: decodeURIComponent(segments[2]) }
    }
    return { view: 'catalog', category: '' }
  }

  if (segments[0] === 'product' && segments[1]) {
    return { view: 'detail', slug: decodeURIComponent(segments[1]) }
  }

  return { view: 'home' }
}

/** Tracks the current view from `location.hash` so catalog/product links are shareable and back/forward work. */
export function useHashRoute(): Route {
  const [route, setRoute] = useState<Route>(() => parseHash(window.location.hash))

  useEffect(() => {
    const onHashChange = () => setRoute(parseHash(window.location.hash))
    window.addEventListener('hashchange', onHashChange)
    return () => window.removeEventListener('hashchange', onHashChange)
  }, [])

  return route
}
