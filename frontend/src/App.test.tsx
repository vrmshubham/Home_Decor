import { render, screen } from '@testing-library/react'
import App from './App'

test('renders homepage with brand and WhatsApp link', () => {
  render(<App />)

  expect(screen.getByText(/\[BRAND NAME\]/i)).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /WhatsApp us/i })).toHaveAttribute('href', expect.stringContaining('https://wa.me/'))
})
