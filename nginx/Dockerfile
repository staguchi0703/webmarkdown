FROM nginx:1.15-alpine

COPY webmarkdown_nginx.conf /etc/nginx/conf.d/webmarkdown_nginx.conf
COPY uwsgi_params /etc/nginx/uwsgi_params
CMD ["nginx", "-g", "daemon off;"]