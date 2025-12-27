SELECT 
	DATE_FORMAT(vv.fecha_venta, '%Y-%m') AS mes_venta,
	CONCAT(pp.categoria, ' - ID: ', pp.id_producto) categoria_id,
	SUM(vv.cantidad) AS total_unidades,
	SUM(vv.cantidad * pp.precio) AS total_ventas
FROM ventas vv
LEFT JOIN productos pp ON vv.id_producto = pp.id_producto 
GROUP BY mes_venta, categoria_id;

SELECT
	cc.nombre nombre_cliente,
	SUM(vv.cantidad) total_unidades_compradas
FROM ventas vv
LEFT JOIN clientes cc ON vv.id_cliente = cc.id_cliente
GROUP BY cc.id_cliente 
ORDER BY total_unidades_compradas DESC
LIMIT 5;