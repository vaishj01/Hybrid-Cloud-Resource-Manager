import api from "../api/api";

export const loginUser = async (formData) => {
    const params = new URLSearchParams();

    params.append("username", formData.username); // this contains the email
    params.append("password", formData.password);

    const response = await api.post(
        "/users/login",
        params,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }
    );

    return response.data;
};