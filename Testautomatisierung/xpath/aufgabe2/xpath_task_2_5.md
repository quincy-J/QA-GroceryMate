# XPath Task 2.5 – Orange Product Elements

## Mengeneingabefeld

```xpath
//div[contains(@class,'product-card')][.//h3='Orange']//input[@type='number']
```

## Add to cart

```xpath
//div[contains(@class,'product-card')][.//h3='Orange']//button[contains(text(),'Add to cart')]
```

## Add to wish list

```xpath
//div[contains(@class,'product-card')][.//h3='Orange']//button[contains(@class,'wishlist')]
```