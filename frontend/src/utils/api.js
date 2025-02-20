import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export const syncPlaylists = async () => {
  const response = await axios.get(`${API_URL}/sync/`);
  return response.data;
};
