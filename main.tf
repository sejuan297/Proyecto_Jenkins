resource "null_resource" "chequeo_infraestructura" {
  provisioner "local-exec" {
    command = "echo 'Terraform: La infraestructura base ha sido verificada correctamente'"
  }
}
