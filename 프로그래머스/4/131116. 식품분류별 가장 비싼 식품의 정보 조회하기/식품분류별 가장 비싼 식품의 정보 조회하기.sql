SELECT F2.CATEGORY, F2.MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT F1 JOIN (SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
                           FROM FOOD_PRODUCT
                           WHERE CATEGORY IN ("과자","국", "김치", "식용유")
                           GROUP BY CATEGORY) AS F2
                           ON F1.CATEGORY = F2.CATEGORY AND F1.PRICE = F2.MAX_PRICE
ORDER BY MAX_PRICE DESC;