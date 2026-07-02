import { useState } from "react";
import { loginUser } from "../services/authService";

function Login() {
    const [formData, setFormData] = useState({
        username: "",
        password: "",
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
    e.preventDefault();

    try {

        const response = await loginUser(formData);

        console.log("Login Successful");
        console.log(response);

        localStorage.setItem(
            "access_token",
            response.access_token
        );

        alert("Login Successful!");

    } catch (error) {

        console.error(error);

        alert("Invalid Username or Password");

    }
};

    return (
        <div>
            <h1>Login</h1>

            <form onSubmit={handleSubmit}>

                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={formData.username}
                    onChange={handleChange}
                />

                <br /><br />

                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                />

                <br /><br />

                <button type="submit">
                    Login
                </button>

            </form>

        </div>
    );
}

export default Login;