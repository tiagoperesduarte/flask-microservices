from app import create_app
from app.utils.env_utils import EnvUtils

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=EnvUtils.get_env('FLASK_RUN_PORT'))
