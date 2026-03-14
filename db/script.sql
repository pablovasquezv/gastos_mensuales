-- 1. Crear la tabla de Categorías
CREATE TABLE IF NOT EXISTS categoria (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    tipo VARCHAR(10) NOT NULL DEFAULT 'GASTO',
    color VARCHAR(7) NOT NULL DEFAULT '#10b981',
    
    -- Campos de Auditoría y Soft Delete
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE NULL,

    CONSTRAINT check_tipo_categoria CHECK (tipo IN ('INGRESO', 'GASTO'))
);

-- 2. Crear la tabla de Gastos (Relacionada con User y Categoria)
CREATE TABLE IF NOT EXISTS gasto (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(200) NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    fecha DATE NOT NULL,
    
    -- Relaciones
    user_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,

    -- Campos de Auditoría y Soft Delete
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE NULL,

    CONSTRAINT fk_gasto_user FOREIGN KEY (user_id) 
        REFERENCES auth_user (id) ON DELETE CASCADE,
    
    CONSTRAINT fk_gasto_categoria FOREIGN KEY (categoria_id) 
        REFERENCES categoria (id) ON DELETE CASCADE
);

-- 3. Índice para mejorar el ordenamiento (como tu ordering = ['-creado_en'])
CREATE INDEX idx_gasto_creado_en ON gasto (creado_en DESC);

-- 4. Datos iniciales de ejemplo para las categorías
INSERT INTO categoria (nombre, tipo, color, created_at, updated_at, deleted_at) VALUES 
('Alimentación', 'GASTO', '#ef4444', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL),
('Transporte', 'GASTO', '#f59e0b', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL),
('Sueldo', 'INGRESO', '#10b981', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL),
('Freelance', 'INGRESO', '#8b5cf6', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL),
('Vivienda', 'GASTO', '#6366f1', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL),
('Salud', 'GASTO', '#ec4899', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL)
ON CONFLICT (nombre) DO NOTHING;

select * from categoria ;

-- Insertar 10 registros de prueba en la tabla gasto
-- Nota: Asegúrate de que user_id=1 existe en auth_user
-- Asumiendo que user_id=1 es tu Admin y las categorías tienen IDs del 1 al 6
INSERT INTO gasto (descripcion, monto, fecha, user_id, categoria_id, created_at, updated_at, deleted_at) VALUES 
('Compra supermercado Lider', 45000.00, '2024-05-01', 1, 1, CURRENT_TIMESTAMP - INTERVAL '10 days', CURRENT_TIMESTAMP - INTERVAL '10 days', NULL),
('Carga de combustible Shell', 35000.00, '2024-05-02', 1, 2, CURRENT_TIMESTAMP - INTERVAL '9 days', CURRENT_TIMESTAMP - INTERVAL '9 days', NULL),
('Pago de Arriendo Mayo', 450000.00, '2024-05-03', 1, 5, CURRENT_TIMESTAMP - INTERVAL '8 days', CURRENT_TIMESTAMP - INTERVAL '8 days', NULL),
('Farmacia - Medicamentos', 12500.00, '2024-05-04', 1, 6, CURRENT_TIMESTAMP - INTERVAL '7 days', CURRENT_TIMESTAMP - INTERVAL '7 days', NULL),
('Almuerzo oficina', 8500.00, '2024-05-05', 1, 1, CURRENT_TIMESTAMP - INTERVAL '6 days', CURRENT_TIMESTAMP - INTERVAL '6 days', NULL),
('Peajes Ruta 68', 4200.00, '2024-05-06', 1, 2, CURRENT_TIMESTAMP - INTERVAL '5 days', CURRENT_TIMESTAMP - INTERVAL '5 days', NULL),
('Cena fin de semana', 28000.00, '2024-05-07', 1, 1, CURRENT_TIMESTAMP - INTERVAL '4 days', CURRENT_TIMESTAMP - INTERVAL '4 days', NULL),
('Suscripción Netflix', 10900.00, '2024-05-08', 1, 5, CURRENT_TIMESTAMP - INTERVAL '3 days', CURRENT_TIMESTAMP - INTERVAL '3 days', NULL),
('Repuesto bicicleta', 15000.00, '2024-05-09', 1, 2, CURRENT_TIMESTAMP - INTERVAL '2 days', CURRENT_TIMESTAMP - INTERVAL '2 days', NULL),
('Antojo Sushi', 22000.00, '2024-05-10', 1, 1, CURRENT_TIMESTAMP - INTERVAL '1 day', CURRENT_TIMESTAMP - INTERVAL '1 day', NULL);


select * from gasto ;
select * from gasto where descripcion ='Esta es una prueba'; 
select * from gasto g WHERE g.deleted_at IS NOT null;
SELECT g.descripcion, g.monto, c.nombre as categoria, g.fecha, a.username 
FROM gasto g
join auth_user a on a.id  = g.user_id 
JOIN categoria c ON g.categoria_id = c.id
ORDER BY g.created_at   DESC;

SELECT 
    g.id, 
    g.descripcion, 
    g.monto, 
    c.nombre AS categoria, 
    g.deleted_at AS fecha_eliminacion
FROM gasto g
JOIN categoria c ON g.categoria_id = c.id
WHERE g.deleted_at IS NOT NULL
ORDER BY g.deleted_at DESC;

