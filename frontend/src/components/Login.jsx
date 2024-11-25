import { useState } from "react"; // Hook para manejar el estado
import { Link, useNavigate } from "react-router-dom"; // Navegación en React Router
import axios from "axios"; // Para realizar solicitudes HTTP
import { Form, Button, Container, Row, Col, Alert } from "react-bootstrap"; // Componentes de UI
import "../styles/LoginStyles.css"; // Estilos personalizados

const Login = () => {
  const [email, setEmail] = useState(""); // Estado para email
  const [password, setPassword] = useState(""); // Estado para password
  const [errorMessage, setErrorMessage] = useState(""); // Mensaje de error
  const navigate = useNavigate(); // Para redirigir a otras páginas

  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMessage("");

    if (!email || !password) {
      setErrorMessage("Both email and password are required.");
      return;
    }

    try {
      const response = await axios.post("http://localhost:8000/api/login/", {
        email,
        password,
      });
      const { access, refresh } = response.data;
      localStorage.setItem("accessToken", access);
      localStorage.setItem("refreshToken", refresh);
      alert("Login successful.");
      navigate("/HomePage");
    } catch (error) {
      setErrorMessage("Invalid email or password."); 
    }
  };

  return (
    <div className="login-container mt-5">
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <h2 className="login-title text-center">Login</h2>

          {errorMessage && <Alert variant="danger">{errorMessage}</Alert>}

          <Form onSubmit={handleLogin}>
            <Form.Group controlId="formEmail" className="login-form-group">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </Form.Group>

            <Form.Group controlId="formPassword" className="login-form-group mt-3">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </Form.Group>

            <Button variant="primary" type="submit" className="login-button mt-4" block>
              Login
            </Button>
          </Form>

          <div className="login-register-link text-center mt-3">
            <Link to="/RegisterPage">No tienes una cuenta? Registrate</Link>
          </div>
        </Col>
      </Row>
    </div>
  );
};

export default Login;
