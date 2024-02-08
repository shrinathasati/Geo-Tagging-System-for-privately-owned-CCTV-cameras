import React from "react";
import "./slide.css";
import "./Home.css";
import CardComponent from "./CardComponenet";


import SlidingPhotoGallery from './slide.jsx'
const Home = () => { 
    const photos = [
        { url: '1.jpeg' },
        { url: '3.jpeg' },
        { url: '2.jpeg' },
        { url: '4.jpg' },
        // Add more photos as needed
    ];
    return (
        <div className="home">
            {/* Include the SlidingPhotoGallery component */}
            <div className="slids">
                <SlidingPhotoGallery photos={photos} loop={ true} />
            </div>
            <h1>Services  </h1>
            <div className="features">
                <CardComponent
                    heading="HIK Form"
                    targetLocation="/"
                />
                <CardComponent
                    heading="Geo Tagging"
                    targetLocation="/"
                />
                <CardComponent
                    heading="Anamoly Detection"
                    targetLocation="http://127.0.0.1:5500/"
                />
                <CardComponent
                    heading="Camera Tempering"
                    targetLocation="/"
                />
                <CardComponent
                    heading="Heat Map Analysis"
                    targetLocation="http://127.0.0.1:5000/"
                />
                <CardComponent
                    heading="Timestamp Analysis"
                    targetLocation="/"
                />
                <CardComponent
                    heading="MultiView Frame"
                    targetLocation="http://127.0.0.1:8080"
                />
            </div> 
            

           
            
        </div>
    )
}

export default Home;