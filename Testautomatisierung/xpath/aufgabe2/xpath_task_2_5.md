# XPath Task 2.5 – Orange Product Elements

## Mengeneingabefeld

```xpath
//div[contains(@class,'product-card')][.//h3='Oranges']//input[@type='number']
```

## Add to cart

```xpath
//div[contains(@class,'product-card')][.//h3='Oranges']//button[contains(text(),'Add to cart')]
```

## Add to wish list

```xpath
//div[contains(@class,'product-card')][.//h3='Oranges']//button[contains(@class,'wishlist')]
```