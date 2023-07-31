$(document).ready(function() {
    $('#edit-profile-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting normally
        var form_data = new FormData(this); // Create a FormData object from the form
        var url = '{% url "edit_profile" %}'; // Replace with your URL
        $.ajax({
            type: 'POST',
            url: url,
            data: form_data,
            processData: false,
            contentType: false,
            beforeSend: function() {
                // Show loading spinner
                $('#save-profile-info').html('<i class="fa fa-spinner fa-spin"></i> Saving...');
            },
            success: function(data) {
                // Hide loading spinner and show success message
                $('#save-profile-info').html('save profile info');
                $('#edit-profile-success-alert').removeClass('d-none').text('Profile updated successfully!');
                $('#edit-profile-error-alert').addClass('d-none');
            },
            error: function(xhr, textStatus, errorThrown) {
                // Hide loading spinner and show error message
                $('#save-profile-info').html('save profile info');
                $('#edit-profile-success-alert').addClass('d-none');
                $('#edit-profile-error-alert').removeClass('d-none').text('Error updating profile: ' + errorThrown);
            }
        });
    });
});
