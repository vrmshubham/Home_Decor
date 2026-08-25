# Product Catalog Setup Guide

## Quick Start — the easy way: edit one file

The whole catalogue (categories, products, prices, stock, descriptions and photos)
is driven from a single file: **`backend/catalogue_data/catalogue.yaml`**. This is
the fastest way to add/remove categories or products, or to change details, prices
and stock counts in bulk.

1. Open `backend/catalogue_data/catalogue.yaml` in any text editor.
2. Add, edit or delete a `categories:` block or a `products:` block under it.
   Removing a block hides that category/product from the storefront (it's marked
   inactive, not deleted — nothing is lost by mistake).
3. Put photos for a product in:
   ```
   backend/media/products/<category-slug>/<product-slug>/
   ```
   Any `.jpg` / `.jpeg` / `.png` / `.webp` file dropped there is linked to the
   product automatically, in filename order (e.g. `01-front.jpg`, `02-detail.jpg`).
4. From the `backend/` folder, run:
   ```bash
   python manage.py sync_catalogue
   ```
   This applies the file to the database. Useful flags:
   - `--dry-run` — preview what would change without saving anything.
   - `--prune` — permanently delete products no longer listed in the file
     (without it, removed products/categories are just hidden, not deleted).

Only a handful of fields (`slug`, `name`, `description`, `material`, price, stock)
are needed for a basic listing — but you can set **any** field that exists on the
`Product` model (fabric details, care instructions, SEO text, etc.) the same way;
see `backend/apps/catalogue/models.py` for the full list.

### Adding photos to product images (recommended: the folder above)

This is the "easy access" path: create a folder named after the category slug and
product slug under `backend/media/products/`, drop image files in, then run
`python manage.py sync_catalogue`. Django serves them at:
```
http://localhost:8000/media/products/<category-slug>/<product-slug>/<filename>
```

### Alternative: Django Admin

For quick one-off edits (e.g. bumping stock after a sale, toggling a product
active/inactive) without opening a text editor, Django Admin works directly on the
database and is unaffected by the YAML file until you next run `sync_catalogue`
(which will overwrite fields the file also manages, using the file's values):

1. Start the Django development server:
   ```bash
   cd backend
   python manage.py runserver
   ```
2. Open Django Admin at: http://localhost:8000/admin/
3. Navigate to **Catalogue > Products** or **Catalogue > Categories**
4. Edit fields directly, or use the **Product Images** / **Product Variants**
   inline sections on a product's edit page to upload images or manage variants.

### Product Details

Each product can have:
- **Basic Info**: Name, Short Name, SKU, Description
- **Classification**: Category, Sub-category, Collection
- **Specifications**: Material, Print Pattern, Color, Size, etc.
- **Pricing**: MRP, Website Price, Compare-at Price
- **Stock**: Current Stock, Lead Time
- **Variants**: Different sizes and colors with individual prices
- **Images**: Multiple product images with alt text

### Frontend Features

#### Home Page
- Hero section
- Category showcase (links to filter products)
- Featured sections

#### Catalog View
- Browse all products or filter by category
- Product cards showing name, material, size, stock, price
- Click "View details" to see full product information

#### Product Detail View
- Full product information
- Image gallery (if multiple images)
- All specifications and variants
- Direct WhatsApp enquiry link with product name pre-filled

### API Endpoints

**Get all categories:**
```
GET http://localhost:8000/api/categories/
```

**Get all products:**
```
GET http://localhost:8000/api/products/
```

**Filter products by category:**
```
GET http://localhost:8000/api/products/?category__slug=curtains
```

**Search products:**
```
GET http://localhost:8000/api/products/?search=curtain
```

### Image Folder Structure

Photos are organized per product, under the category slug:
```
backend/media/products/
├── curtains/
│   └── ivory-linen-curtains/
│       ├── 01-front.jpg
│       └── 02-detail.jpg
├── bedsheets/
│   └── sandstone-stripe-bedsheet/
│       └── 01-front.jpg
└── rugs/
    └── terracotta-weave-rug/
        └── 01-front.jpg
```
Filenames sort alphabetically to decide display order, so prefix them (`01-`, `02-`, ...)
if order matters. After adding files, run `python manage.py sync_catalogue` to link them.

### Troubleshooting

**Images not showing:**
- Ensure DEBUG = True in `backend/config/settings/development.py`
- Check the folder is named exactly `<category-slug>/<product-slug>` under `backend/media/products/`
- Re-run `python manage.py sync_catalogue` after adding files — images are only linked on sync

**Category or product not appearing / not updating:**
- Confirm the block exists (and isn't accidentally removed) in `backend/catalogue_data/catalogue.yaml`
- Run `python manage.py sync_catalogue` — edits to the file only take effect after a sync
- Removed blocks are hidden (`is_active=False`), not deleted; re-add the block and sync to bring them back
- Check Django admin > Catalogue for the current active/inactive state

### Configuration Files

Key configuration files:
- `backend/catalogue_data/catalogue.yaml` - The catalogue itself: categories, products, prices, stock, descriptions
- `backend/apps/catalogue/management/commands/sync_catalogue.py` - Applies the YAML file to the database
- `backend/config/settings/base.py` - Media file settings
- `backend/config/urls.py` - Media file serving in DEBUG mode
- `backend/.gitignore` - Ignores media files from git
- `frontend/src/App.tsx` - Frontend app logic and API calls
- `frontend/src/styles.css` - Styling for all views

### Environment Variables

In `backend/.env` (development):
```
DJANGO_SETTINGS_MODULE=config.settings.development
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

In `frontend/.env.local` (optional):
```
VITE_API_URL=http://localhost:8000/api
VITE_WHATSAPP_NUMBER=919999999999
```

## Next Steps

1. Edit `backend/catalogue_data/catalogue.yaml` to add/change categories and products
2. Drop product photos into `backend/media/products/<category-slug>/<product-slug>/`
3. Run `python manage.py sync_catalogue` to apply changes
4. Test category filtering by clicking on categories on the storefront
5. View product details by clicking "View details" on product cards

Enjoy your new home décor storefront!
