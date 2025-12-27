CREATE DATABASE prueba_ventas CHARACTER SET utf8 COLLATE utf8_general_ci;

USE prueba_ventas;

CREATE TABLE clientes (
	id_cliente INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(80),
	ciudad VARCHAR(30),
	fecha_registro DATE,
	PRIMARY KEY (id_cliente)
);

CREATE TABLE productos (
	id_producto INT NOT NULL AUTO_INCREMENT,
	categoria VARCHAR(50),
	precio DECIMAL(10,2),
	PRIMARY KEY (id_producto)
);

CREATE TABLE ventas (
	id_venta INT NOT NULL AUTO_INCREMENT,
	id_cliente INT NOT NULL,
	id_producto INT NOT NULL,
	fecha_venta DATE,
	cantidad INT,
	PRIMARY KEY (id_venta),
    INDEX idx_ventas_cliente_fecha (id_cliente, fecha_venta),
    INDEX idx_ventas_producto_fecha (id_producto, fecha_venta),
    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (id_producto) REFERENCES productos (id_producto) ON UPDATE CASCADE ON DELETE RESTRICT
);