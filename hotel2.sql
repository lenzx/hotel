-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-06-2023 a las 21:30:13
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hotel2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `RUT_ADMINISTRADOR` char(20) NOT NULL,
  `CONTRASENA` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `costo_habitacion`
--

CREATE TABLE `costo_habitacion` (
  `ID_COSTO_HABITACION` int(11) NOT NULL,
  `ID_TIPO_HABITACION` int(11) NOT NULL,
  `COSTO_BASE` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `costo_habitacion`
--

INSERT INTO `costo_habitacion` (`ID_COSTO_HABITACION`, `ID_TIPO_HABITACION`, `COSTO_BASE`) VALUES
(1, 1, 10000),
(2, 2, 20000),
(3, 3, 30000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encargado`
--

CREATE TABLE `encargado` (
  `RUT_ENCARGADO` char(20) NOT NULL,
  `CONTRASENA` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitacion`
--

CREATE TABLE `habitacion` (
  `N_HABITACION` int(11) NOT NULL,
  `ID_TIPO_HABITACION` int(11) NOT NULL,
  `CAPACIDAD_MAX` int(11) NOT NULL,
  `ORIENTACION` char(20) NOT NULL,
  `MIN_PASAJERO` int(11) NOT NULL,
  `HABILITAR` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `habitacion`
--

INSERT INTO `habitacion` (`N_HABITACION`, `ID_TIPO_HABITACION`, `CAPACIDAD_MAX`, `ORIENTACION`, `MIN_PASAJERO`, `HABILITAR`) VALUES
(1, 3, 4, 'sur', 2, 1),
(2, 1, 10, 'norte', 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscribe`
--

CREATE TABLE `inscribe` (
  `ID_REGISTRO` int(11) NOT NULL,
  `RUT_PASAJERO` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pasajero`
--

CREATE TABLE `pasajero` (
  `RUT_PASAJERO` char(20) NOT NULL,
  `NOMBRE` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pasajero`
--

INSERT INTO `pasajero` (`RUT_PASAJERO`, `NOMBRE`) VALUES
('111111', 'jose salgado'),
('222222', 'matias plaza');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

CREATE TABLE `registro` (
  `ID_REGISTRO` int(11) NOT NULL,
  `N_HABITACION` int(11) NOT NULL,
  `RUT_PASAJERO_RESPONSABLE` char(20) NOT NULL,
  `FECHA_ASIGNACION` date NOT NULL,
  `HORA_ASIGNACION` time NOT NULL,
  `FECHA_FIN` date NOT NULL,
  `HORA_FIN` time NOT NULL,
  `N_PERSONAS` int(11) NOT NULL,
  `COSTO_ADICIONAL_PERSONA` float NOT NULL,
  `COSTO_TOTAL` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_habitacion`
--

CREATE TABLE `tipo_habitacion` (
  `ID_TIPO_HABITACION` int(11) NOT NULL,
  `TIPO_HABITACION` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_habitacion`
--

INSERT INTO `tipo_habitacion` (`ID_TIPO_HABITACION`, `TIPO_HABITACION`) VALUES
(1, 'VIP'),
(2, 'Comun'),
(3, 'Suite');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`RUT_ADMINISTRADOR`);

--
-- Indices de la tabla `costo_habitacion`
--
ALTER TABLE `costo_habitacion`
  ADD PRIMARY KEY (`ID_COSTO_HABITACION`),
  ADD KEY `FK_PRECIO` (`ID_TIPO_HABITACION`);

--
-- Indices de la tabla `encargado`
--
ALTER TABLE `encargado`
  ADD PRIMARY KEY (`RUT_ENCARGADO`);

--
-- Indices de la tabla `habitacion`
--
ALTER TABLE `habitacion`
  ADD PRIMARY KEY (`N_HABITACION`),
  ADD KEY `FK_PERTENECE` (`ID_TIPO_HABITACION`);

--
-- Indices de la tabla `inscribe`
--
ALTER TABLE `inscribe`
  ADD PRIMARY KEY (`ID_REGISTRO`,`RUT_PASAJERO`),
  ADD KEY `FK_INSCRIBE2` (`RUT_PASAJERO`);

--
-- Indices de la tabla `pasajero`
--
ALTER TABLE `pasajero`
  ADD PRIMARY KEY (`RUT_PASAJERO`);

--
-- Indices de la tabla `registro`
--
ALTER TABLE `registro`
  ADD PRIMARY KEY (`ID_REGISTRO`),
  ADD KEY `FK_REGISTRA` (`N_HABITACION`),
  ADD KEY `FK_RESPONSABILIZA` (`RUT_PASAJERO_RESPONSABLE`);

--
-- Indices de la tabla `tipo_habitacion`
--
ALTER TABLE `tipo_habitacion`
  ADD PRIMARY KEY (`ID_TIPO_HABITACION`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registro`
--
ALTER TABLE `registro`
  MODIFY `ID_REGISTRO` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `costo_habitacion`
--
ALTER TABLE `costo_habitacion`
  ADD CONSTRAINT `FK_PRECIO` FOREIGN KEY (`ID_TIPO_HABITACION`) REFERENCES `tipo_habitacion` (`ID_TIPO_HABITACION`);

--
-- Filtros para la tabla `habitacion`
--
ALTER TABLE `habitacion`
  ADD CONSTRAINT `FK_PERTENECE` FOREIGN KEY (`ID_TIPO_HABITACION`) REFERENCES `tipo_habitacion` (`ID_TIPO_HABITACION`);

--
-- Filtros para la tabla `inscribe`
--
ALTER TABLE `inscribe`
  ADD CONSTRAINT `FK_INSCRIBE` FOREIGN KEY (`ID_REGISTRO`) REFERENCES `registro` (`ID_REGISTRO`),
  ADD CONSTRAINT `FK_INSCRIBE2` FOREIGN KEY (`RUT_PASAJERO`) REFERENCES `pasajero` (`RUT_PASAJERO`);

--
-- Filtros para la tabla `registro`
--
ALTER TABLE `registro`
  ADD CONSTRAINT `FK_REGISTRA` FOREIGN KEY (`N_HABITACION`) REFERENCES `habitacion` (`N_HABITACION`),
  ADD CONSTRAINT `FK_RESPONSABILIZA` FOREIGN KEY (`RUT_PASAJERO_RESPONSABLE`) REFERENCES `pasajero` (`RUT_PASAJERO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
