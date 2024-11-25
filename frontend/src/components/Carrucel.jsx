import { useState, useEffect } from 'react';
import { Carousel } from 'react-bootstrap';
import axios from 'axios';
import '../styles/CarrucelStyles.css';

function Carrusel() {
    const [imagenes, setImagenes] = useState([]);
    const [index, setIndex] = useState(0);

    const handleSelect = (selectedIndex) => {
        setIndex(selectedIndex);
    };


    useEffect(() => {
        const fetchImages = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/carrusel/'); 
                setImagenes(response.data);
            } catch (error) {
                console.error('Error al obtener las imágenes:', error);
            }
        };
        fetchImages();
    }, []);

    return (
        <Carousel
            activeIndex={index}
            onSelect={handleSelect}
            className="custom_carousel"
        >
            {imagenes.map((item) => (
                <Carousel.Item key={item.id}>
                    <img
                        className="d-block w-100"
                        src={`http://localhost:8000${item.imagen}`} // URL completa de la imagen
                        alt={item.titulo || 'Carrusel'}
                    />
                    {item.titulo && (
                        <Carousel.Caption>
                            <h3>{item.titulo}</h3>
                        </Carousel.Caption>
                    )}
                </Carousel.Item>
            ))}
        </Carousel>
    );
}

export default Carrusel;
