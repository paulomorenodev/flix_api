const URL = 'https://dummyjson.com/products';
const URL2= 'http://127.0.0.1:8000/actors/';

async function chamarApi() {
    const resp = await fetch(URL2);
    console.log(resp);
    if (resp.status === 200) {
        const data = await resp.json();
    console.log(data);
    }
    
}

chamarApi()