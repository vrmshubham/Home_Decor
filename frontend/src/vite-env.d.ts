/// <reference types="vite/client" />

declare global {
  interface ImportMetaEnv {
    readonly VITE_WHATSAPP_NUMBER: string
    readonly VITE_API_BASE_URL?: string
    readonly [key: string]: string | boolean | undefined
  }

  interface ImportMeta {
    readonly env: ImportMetaEnv
  }
}

export {}
