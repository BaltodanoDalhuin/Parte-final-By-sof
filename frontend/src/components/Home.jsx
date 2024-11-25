import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/HomeStyles.css';

const Home = () => {
  const [content, setContent] = useState(null);

  useEffect(() => {
    const fetchContent = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/home-content/');
        setContent(response.data);
      } catch (error) {
        console.error('Error fetching home content:', error);
      }
    };

    fetchContent();
  }, []);

  if (!content) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div className="content">
        <div className="text">
          <h1>{content.title}</h1>
          <p>{content.description}</p>
        </div>

        <div className="image">
          <img src={`http://localhost:8000${content.image}`} alt="Home preview" />
        </div>
      </div>
    </div>
  );
};

export default Home;
