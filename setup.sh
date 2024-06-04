mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"babar63101@gmai.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
