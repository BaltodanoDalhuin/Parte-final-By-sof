import { useState, useEffect } from "react";
import { Container, Row, Col } from "react-bootstrap";
import { FaWhatsapp, FaInstagram, FaMapMarkerAlt } from "react-icons/fa";
import "../styles/Footer.css";

const Footer = () => {
  const [links, setLinks] = useState([]);

  useEffect(() => {
    const fetchFooterLinks = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/footer-links/");
        const data = await response.json();
        setLinks(data);
      } catch (error) {
        console.error("Error al obtener los enlaces del footer:", error);
      }
    };
    fetchFooterLinks();
  }, []);

  const socialLinks = links.filter((link) => link.is_social);
  const regularLinks = links.filter((link) => !link.is_social);

  return (
    <footer className="footer bg-dark text-white">
      <Container>
        <Row className="mb-4">
          <Col md={4} className="text-center text-md-left mb-3 mb-md-0">
            <h5>Información</h5>
            <p>
              Si quieres saber más de nosotros o de nuestros productos, por
              favor comunícate por medio de nuestras redes sociales.
            </p>
          </Col>

          <Col md={4} className="text-center text-md-left mb-3 mb-md-0">
            <h5>Enlaces</h5>
            <ul className="list-unstyled">
              {regularLinks.map((link) => (
                <li key={link.id}>
                  <a
                    href={link.url}
                    className="text-white"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </Col>

          <Col md={4} className="text-center">
            <h5>Redes Sociales</h5>
            <Row className="justify-content-center">
              {socialLinks.map((link) => (
                <Col xs="auto" key={link.id} className="footer-icon-col mb-3">
                  <a
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="footer-icon"
                  >
                    {link.name === "WhatsApp" && (
                      <>
                        <FaWhatsapp className="footer-icon-img" />
                        <span className="footer-icon-text">WhatsApp</span>
                      </>
                    )}
                    {link.name === "Instagram" && (
                      <>
                        <FaInstagram className="footer-icon-img" />
                        <span className="footer-icon-text">Instagram</span>
                      </>
                    )}
                    {link.name === "Dirección" && (
                      <>
                        <FaMapMarkerAlt className="footer-icon-img" />
                        <span className="footer-icon-text">Dirección</span>
                      </>
                    )}
                  </a>
                </Col>
              ))}
            </Row>
          </Col>
        </Row>

        <Row>
          <Col className="text-center">
            <p>
              &copy; {new Date().getFullYear()} By | Sof. Todos los derechos
              reservados.
            </p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
