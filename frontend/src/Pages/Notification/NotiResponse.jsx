import React from 'react';

const ResponseForm = () => {
    return (
        <div>
            <div class="logo"></div>

            <h2>HIK App Details Submission</h2>

            <form action="submit_details.php" method="post" enctype="multipart/form-data">
                <label for="mobileNumber">Mobile Number:</label>
                <input type="tel" id="mobileNumber" name="mobileNumber" required />

                    <label for="userNumber">User Number:</label>
                    <input type="text" id="userNumber" name="userNumber" required />

                        <label for="password">Password:</label>
                        <input type="password" id="password" name="password" required />

                            <label for="qrCode">QR Code:</label>
                            <input type="file" id="qrCode" name="qrCode" accept="image/*" required />

                                <input type="submit" value="Submit" />
                                </form>
        </div>
    );
};

export default ResponseForm;
