# Product Catalog Setup Guide

## Quick Start

### 1. Folder Structure for Product Images

Product images should be placed in:
```
backend/media/products/
```

This folder is already created and configured. Django will serve these images at:
```
http://localhost:8000/media/products/[filename]
```

### 2. Adding Product Images via Django Admin

1. Start the Django development server:
   ```bash
   cd backend
   python manage.py runserver
   ```

2. Open Django Admin at: http://localhost:8000/admin/
3. Navigate to **Catalogue > Products**
4. Select a product to edit
5. Scroll down to **Product Images** section
6. Click **Add another Product Image**
7. Upload image and fill in the alt text
8. Save the product

### 3. Category Filtering

Categories are automatically fetched from the database and displayed on the storefront.

To add categories:
1. Go to Django Admin > Catalogue > Categories
2. Add a new category with:
   - Name (e.g., "Curtains")
   - Slug (e.g., "curtains")
   - Description
   - Mark as active

### 4. Product Details

Each product can have:
- **Basic Info**: Name, Short Name, SKU, Description
- **Classification**: Category, Sub-category, Collection
- **Specifications**: Material, Print Pattern, Color, Size, etc.
- **Pricing**: MRP, Website Price, Compare-at Price
- **Stock**: Current Stock, Lead Time
- **Variants**: Different sizes and colors with individual prices
- **Images**: Multiple product images with alt text

### 5. Frontend Features

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

### 6. API Endpoints

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

### 7. Image Upload Path Examples

Recommended folder structure for organizing images:
```
backend/media/products/
├── curtains/
│   ├── curtain_001_primary.jpg
│   ├── curtain_001_variant2.jpg
│   └── curtain_002_primary.jpg
├── bedsheets/
│   ├── bedsheet_001_primary.jpg
│   └── bedsheet_002_primary.jpg
└── rugs/
    └── rug_001_primary.jpg
```

### 8. Troubleshooting

**Images not showing:**
- Ensure DEBUG = True in `backend/config/settings/development.py`
- Check that image path in ProductImage model is correct
- Verify image file exists in `backend/media/products/`

**Category filtering not working:**
- Ensure category slug is correct
- Check that products are linked to the category
- Verify category is marked as active

**Products not appearing:**
- Check that products are marked as active
- Verify products have a category assigned
- Check Django admin > Catalogue > Products for the products

### 9. Configuration Files

Key configuration files:
- `backend/config/settings/base.py` - Media file settings
- `backend/config/urls.py` - Media file serving in DEBUG mode
- `backend/.gitignore` - Ignores media files from git
- `frontend/src/App.tsx` - Frontend app logic and API calls
- `frontend/src/styles.css` - Styling for all views

### 10. Environment Variables

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

1. Place product images in `backend/media/products/`
2. Add/edit categories in Django admin
3. Add/edit products with images and specifications
4. Test category filtering by clicking on categories on the storefront
5. View product details by clicking "View details" on product cards

Enjoy your new home décor storefront!
