from src.controllers.pet_deleter_controller import PetDeleterController

def test_delete(mocker):
    mock_repository = mocker.Mock()
    controller = PetDeleterController(mock_repository)

    controller.delete("amiguinho")

    mock_repository.delete_pets.assert_called_once_with("amiguinho")
