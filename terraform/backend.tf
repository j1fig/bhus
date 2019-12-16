terraform {
  backend "remote" {
    organization = "j1fig"

    workspaces {
      name = "tldx"
    }
  }
}
