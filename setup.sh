mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"habibi.alireza2010@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
