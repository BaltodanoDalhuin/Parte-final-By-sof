import { Button, Table, Container, Row, Col, Form } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import axios from 'axios'; // Librería para hacer peticiones HTTP

const Admin = () => {
  const API_URL = 'http://localhost:8000/productos/'; 

  const [productos, setProductos] = useState([]);
  const [nombre, setNombre] = useState('');
  const [marca, setMarca] = useState('');
  const [categoria, setCategoria] = useState('');
  const [precio, setPrecio] = useState('');
  const [imagen, setImagen] = useState('');
  const [editingIndex, setEditingIndex] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagen(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const nuevoProducto = { nombre, marca, categoria, precio, imagen };

    try {
      if (editingIndex !== null) {
        // Actualizar producto existente
        const id = productos[editingIndex].id;
        await axios.put(`${API_URL}${id}/`, nuevoProducto);
        setEditingIndex(null);
      } else {
        // Crear nuevo producto
        await axios.post(API_URL, nuevoProducto);
      }
      resetForm();
      fetchProductos();
    } catch (error) {
      console.error('Error al enviar los datos:', error);
    }
  };

  const fetchProductos = async () => {
    try {
      const response = await axios.get(API_URL);
      setProductos(response.data);
    } catch (error) {
      console.error('Error al obtener los productos:', error);
    }
  };

  const handleEdit = (index) => {
    const producto = productos[index];
    setNombre(producto.nombre);
    setMarca(producto.marca);
    setCategoria(producto.categoria);
    setPrecio(producto.precio);
    setImagen(producto.imagen);
    setEditingIndex(index);
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API_URL}${id}/`);
      fetchProductos();
    } catch (error) {
      console.error('Error al eliminar el producto:', error);
    }
  };

  const resetForm = () => {
    setNombre('');
    setMarca('');
    setCategoria('');
    setPrecio('');
    setImagen('');
  };

  useEffect(() => {
    fetchProductos();
  }, []);

  return (
    <Container>
      <h1 className="text-center my-4">Products</h1>

      <Form onSubmit={handleSubmit} className="mb-4">
        <Row>
          <Col>
            <Form.Control 
              type="text" 
              placeholder="Nombre" 
              value={nombre} 
              onChange={(e) => setNombre(e.target.value)} 
              required 
            />
          </Col>
          <Col>
            <Form.Control 
              type="text" 
              placeholder="Marca" 
              value={marca} 
              onChange={(e) => setMarca(e.target.value)} 
              required 
            />
          </Col>
          <Col>
            <Form.Control 
              type="text" 
              placeholder="Categoría" 
              value={categoria} 
              onChange={(e) => setCategoria(e.target.value)} 
              required 
            />
          </Col>
          <Col>
            <Form.Control 
              type="number" 
              placeholder="Precio" 
              value={precio} 
              onChange={(e) => setPrecio(e.target.value)} 
              required 
            />
          </Col>
          <Col>
            <Form.Control 
              type="file" 
              accept="image/*" 
              onChange={handleFileChange} 
              required 
            />
          </Col>
          <Col>
            <Button type="submit" variant="primary">
              {editingIndex !== null ? 'Actualizar Producto' : 'Agregar Producto'}
            </Button>
          </Col>
        </Row>
      </Form>

      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Marca</th>
            <th>Categoría</th>
            <th>Precio</th>
            <th>Imagen</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          {productos.map((producto, index) => (
            <tr key={producto.id}>
              <td>{producto.id}</td>
              <td>{producto.nombre}</td>
              <td>{producto.marca}</td>
              <td>{producto.categoria}</td>
              <td>{producto.precio}$</td>
              <td>
                <img src={producto.imagen} alt={producto.nombre} width="50" />
              </td>
              <td>
                <Button variant="primary" size="sm" className="me-2" onClick={() => handleEdit(index)}>Edit</Button>
                <Button variant="danger" size="sm" onClick={() => handleDelete(producto.id)}>Delete</Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default AdminForm;
