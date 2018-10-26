param([String]$SQLALCHEMY_URI='postgresql://postgres@localhost/xml_db',[String]$SECRET_KEY='vvvkbj>?tt')
Write-Host 'Setting up the database url env variable...'
$env:SQLALCHEMY_URI=$SQLALCHEMY_URI
Write-Host 'Setting up the secret key env variable...'
$env:SECRET_KEY=$SECRET_KEY

Write-Host "$SQLALCHEMY_URI & $SECRET_KEY"
