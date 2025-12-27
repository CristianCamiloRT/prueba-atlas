INSERT INTO clientes (nombre, ciudad, fecha_registro)
VALUES
('Juan Pérez', 'Bogotá', '2023-01-15'),
('María López', 'Medellín', '2023-02-20'),
('Carlos Gómez', 'Cali', '2023-03-05'),
('Ana Torres', 'Bogotá', '2023-03-25'),
('Luis Ramírez', 'Barranquilla', '2023-04-10');

INSERT INTO productos (categoria, precio)
VALUES
('Electrónica', 500.00),
('Electrónica', 1500.00),
('Hogar', 200.00),
('Hogar', 750.00),
('Ropa', 100.00);

INSERT INTO ventas (id_cliente, id_producto, fecha_venta, cantidad)
VALUES
(1, 1, '2023-05-01', 2),
(1, 3, '2023-05-15', 1),
(2, 1, '2023-06-05', 1),
(3, 3, '2023-06-20', 3),
(3, 1, '2023-06-25', 1),
(4, 5, '2023-07-10', 4),
(5, 1, '2023-07-15', 2),
(5, 2, '2023-07-20', 1);