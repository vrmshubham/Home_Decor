import { fireEvent, render, screen } from '@testing-library/react'
import { afterEach, test } from 'vitest'
import App from './App'

afterEach(() => {
  window.location.hash = ''
})

test('renders homepage with brand and WhatsApp link', () => {
  render(<App />)

  expect(screen.getByRole('link', { name: /\[BRAND NAME\]/i })).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /WhatsApp us/i })).toHaveAttribute('href', expect.stringContaining('https://wa.me/'))
})

test('mobile nav toggle opens and closes the menu', () => {
  render(<App />)

  const toggle = screen.getByRole('button', { name: /open menu/i })
  expect(toggle).toHaveAttribute('aria-expanded', 'false')

  fireEvent.click(toggle)
  expect(screen.getByRole('button', { name: /close menu/i })).toHaveAttribute('aria-expanded', 'true')

  fireEvent.click(screen.getByRole('button', { name: /close menu/i }))
  expect(screen.getByRole('button', { name: /open menu/i })).toHaveAttribute('aria-expanded', 'false')
})

test('navigating to #/products shows the product catalog', () => {
  window.location.hash = '#/products'
  render(<App />)

  expect(screen.getByRole('heading', { name: /all products/i })).toBeInTheDocument()
})
