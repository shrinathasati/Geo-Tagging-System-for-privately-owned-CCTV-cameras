import React from 'react';
import { useNavigate } from 'react-router-dom';
import "./CardComponent.css";

const CardComponent = ({ heading, targetLocation }) => {
    const navigate = useNavigate();


    const handleButtonClick = () => {
        // Change the location of the page when the button is clicked
        navigate(targetLocation);
    };

    return (
        <div className="card">
            <div className="card-header">
                <h2>{heading}</h2>
            </div>
            <div className="card-body">
                {/* Additional content can be added here if needed */}
            </div>
            <a href={targetLocation}  target="_blank" className="card-footer">
                <button onClick={handleButtonClick}>Read More</button>
            </a>
        </div>
    );
};

export default CardComponent;
