module.exports = {
  apps: [
    {
      name: 'LLMAPI',
      cwd: './',
      interpreter: 'python3',
      script: 'app.py',
      instances: 'max',
      watch: false,
      env: {
        NODE_ENV: 'prod'
      },
      exec_mode: 'fork',
      max_memory_restart: '1024M',
      log_date_format: 'YYYY-MM-DD HH:mZ'
    }
  ]
}