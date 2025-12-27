CREATE VIEW clientes_compras AS
SELECT 
	cc.nombre nombre_cliente,
	cc.ciudad ciudad_cliente,
	COUNT(*) total_compras,
	MAX(vv.fecha_venta) fecha_ultima_compra
FROM clientes cc
LEFT JOIN ventas vv ON cc.id_cliente = vv.id_cliente
GROUP BY cc.id_cliente;